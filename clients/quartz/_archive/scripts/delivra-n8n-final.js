// Quartz Delivra CPES Tracker — All-in-One
var BASE_URL = "https://integration.delivra.com/DelivraRESTServices/Services.svc";
var USERNAME = "aroggio+newsletter-ops@qz.com";
var PASSWORD = "N3ws-Qu@rtz-Ops";
var LISTNAME = "quartz-prod";
var BAKEOFF_START = "2026-02-01";
var SAMPLE_SIZE = 50;

var AGENCIES = [
  { name: "TFM", category_id: 623803, category_name: "feed-media" },
  { name: "BG", category_id: 623802, category_name: "boletin" },
  { name: "GL", category_id: 601833, category_name: "paid-acquisition" }
];

var results = [];
var today = new Date().toISOString().split("T")[0];

for (var i = 0; i < AGENCIES.length; i++) {
  var agency = AGENCIES[i];

  var allContacts = [];
  try {
    var resp = await helpers.request({
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
  } catch (err) {
    results.push({ json: { date: today, agency: agency.name, error: err.message } });
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

  // Sample contacts for status check
  var sampleCount = Math.min(SAMPLE_SIZE, bakeoffContacts.length);
  var shuffled = bakeoffContacts.slice().sort(function() { return 0.5 - Math.random(); });
  var sample = shuffled.slice(0, sampleCount);

  var active = 0;
  var held = 0;
  var unsub = 0;
  var other = 0;
  var engagedCount = 0;
  var checkedCount = 0;

  for (var k = 0; k < sample.length; k++) {
    try {
      var detail = await helpers.request({
        method: "GET",
        url: BASE_URL + "/Contacts/" + sample[k].MemberID_,
        headers: {
          "username": USERNAME,
          "password": PASSWORD,
          "listname": LISTNAME
        },
        json: true
      });
      var d = Array.isArray(detail) ? detail[0] : detail;
      var mtype = (d.MemberType || "").toLowerCase();
      var engagement = parseFloat(d.Engagement || "0");
      if (mtype === "normal") active++;
      else if (mtype === "held") held++;
      else if (mtype === "unsub") unsub++;
      else other++;
      if (engagement > 0) engagedCount++;
      checkedCount++;
    } catch (err) {
      other++;
      checkedCount++;
    }
  }

  var denom = Math.max(checkedCount, 1);
  var activeRate = (active / denom * 100).toFixed(1);
  var heldRate = (held / denom * 100).toFixed(1);
  var engagedRate = (engagedCount / denom * 100).toFixed(1);
  var estActive = Math.round(bakeoffContacts.length * active / denom);
  var estHeld = Math.round(bakeoffContacts.length * held / denom);
  var estEngaged = Math.round(bakeoffContacts.length * engagedCount / denom);

  results.push({
    json: {
      date: today,
      agency: agency.name,
      category: agency.category_name,
      total_in_tag: allContacts.length,
      bakeoff_subs: bakeoffContacts.length,
      feb_subs: feb,
      mar_subs: mar,
      sample_size: checkedCount,
      sample_active: active,
      sample_held: held,
      sample_unsub: unsub,
      sample_engaged: engagedCount,
      active_rate_pct: activeRate,
      held_rate_pct: heldRate,
      engaged_rate_pct: engagedRate,
      est_active_total: estActive,
      est_held_total: estHeld,
      est_engaged_total: estEngaged
    }
  });
}

return results;
