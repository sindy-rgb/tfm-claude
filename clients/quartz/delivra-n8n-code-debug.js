// Quartz Delivra CPES Tracker — DEBUG VERSION
var config = $input.first().json;
var results = [];
var today = new Date().toISOString().split("T")[0];

// Debug: confirm config loaded
console.log("Config loaded. Agencies: " + config.AGENCIES.length);
console.log("Base URL: " + config.BASE_URL);
console.log("Username: " + config.USERNAME);

// First just try one API call to test connectivity
var testUrl = config.BASE_URL + "/Categories/" + config.AGENCIES[0].category_id + "/Contacts";
console.log("Test URL: " + testUrl);

try {
  var testResp = await $http.request({
    method: "GET",
    url: testUrl,
    headers: {
      "username": config.USERNAME,
      "password": config.PASSWORD,
      "listname": config.LISTNAME
    },
    json: true
  });
  console.log("Test call succeeded. Got " + (Array.isArray(testResp) ? testResp.length : "non-array") + " contacts");
} catch (err) {
  console.log("TEST CALL FAILED: " + err.message);
  console.log("Error details: " + JSON.stringify(err));
  return [{ json: { error: "API call failed", message: err.message, url: testUrl } }];
}

// If test passed, do the full run
for (var i = 0; i < config.AGENCIES.length; i++) {
  var agency = config.AGENCIES[i];
  console.log("--- Agency: " + agency.name + " ---");

  var allContacts = [];
  try {
    var resp = await $http.request({
      method: "GET",
      url: config.BASE_URL + "/Categories/" + agency.category_id + "/Contacts",
      headers: {
        "username": config.USERNAME,
        "password": config.PASSWORD,
        "listname": config.LISTNAME
      },
      json: true
    });
    allContacts = Array.isArray(resp) ? resp : [];
    console.log(agency.name + " contacts fetched: " + allContacts.length);
  } catch (err) {
    console.log(agency.name + " FETCH ERROR: " + err.message);
    continue;
  }

  var bakeoffContacts = [];
  for (var j = 0; j < allContacts.length; j++) {
    var joined = (allContacts[j].DateJoined || "").substring(0, 10);
    if (joined >= config.BAKEOFF_START && allContacts[j].MemberID_ !== 0) {
      bakeoffContacts.push(allContacts[j]);
    }
  }

  var feb = 0;
  var mar = 0;
  for (var j = 0; j < bakeoffContacts.length; j++) {
    if (bakeoffContacts[j].DateJoined.indexOf("2026-02") === 0) feb++;
    if (bakeoffContacts[j].DateJoined.indexOf("2026-03") === 0) mar++;
  }

  console.log(agency.name + " bakeoff: " + bakeoffContacts.length + " (Feb:" + feb + " Mar:" + mar + ")");

  // Skip contact sampling for now — just get the counts
  results.push({
    json: {
      date: today,
      agency: agency.name,
      category: agency.category_name,
      total_in_tag: allContacts.length,
      bakeoff_subs: bakeoffContacts.length,
      feb_subs: feb,
      mar_subs: mar,
      sample_size: 0,
      sample_active: 0,
      sample_held: 0,
      sample_unsub: 0,
      sample_engaged: 0,
      active_rate_pct: "0",
      held_rate_pct: "0",
      engaged_rate_pct: "0",
      est_active_total: 0,
      est_held_total: 0,
      est_engaged_total: 0
    }
  });
}

console.log("Done. Returning " + results.length + " rows");
return results;
