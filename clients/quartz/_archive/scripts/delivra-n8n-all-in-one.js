// Quartz Delivra CPES Tracker — All-in-One
var BASE_URL = "https://integration.delivra.com/DelivraRESTServices/Services.svc";
var USERNAME = "aroggio+newsletter-ops@qz.com";
var PASSWORD = "N3ws-Qu@rtz-Ops";
var LISTNAME = "quartz-prod";
var BAKEOFF_START = "2026-02-01";

var AGENCIES = [
  { name: "TFM", category_id: 623803, category_name: "feed-media" },
  { name: "BG", category_id: 623802, category_name: "boletin" },
  { name: "GL", category_id: 601833, category_name: "paid-acquisition" }
];

var results = [];
var today = new Date().toISOString().split("T")[0];

for (var i = 0; i < AGENCIES.length; i++) {
  var agency = AGENCIES[i];
  console.log("--- " + agency.name + " ---");

  var allContacts = [];
  try {
    var resp = await $http.request({
      method: "GET",
      url: BASE_URL + "/Categories/" + agency.category_id + "/Contacts",
      headers: {
        "username": USERNAME,
        "password": PASSWORD,
        "listname": LISTNAME
      },
      json: true
    });
    allContacts = Array.isArray(resp) ? resp : [];
    console.log(agency.name + " contacts: " + allContacts.length);
  } catch (err) {
    console.log(agency.name + " ERROR: " + err.message);
    continue;
  }

  var bakeoffContacts = [];
  for (var j = 0; j < allContacts.length; j++) {
    var joined = (allContacts[j].DateJoined || "").substring(0, 10);
    if (joined >= BAKEOFF_START && allContacts[j].MemberID_ !== 0) {
      bakeoffContacts.push(allContacts[j]);
    }
  }

  var feb = 0;
  var mar = 0;
  for (var j = 0; j < bakeoffContacts.length; j++) {
    if (bakeoffContacts[j].DateJoined.indexOf("2026-02") === 0) feb++;
    if (bakeoffContacts[j].DateJoined.indexOf("2026-03") === 0) mar++;
  }

  console.log(agency.name + " bakeoff: " + bakeoffContacts.length);

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

console.log("Done. Rows: " + results.length);
return results;
