// MINIMAL TEST — using fetch instead of $http
var url = "https://integration.delivra.com/DelivraRESTServices/Services.svc/Categories/623803/Contacts";

try {
  var response = await fetch(url, {
    method: "GET",
    headers: {
      "username": "aroggio+newsletter-ops@qz.com",
      "password": "N3ws-Qu@rtz-Ops",
      "listname": "quartz-prod"
    }
  });

  var text = await response.text();
  var data = JSON.parse(text.replace(/^\uFEFF/, ""));
  var count = Array.isArray(data) ? data.length : 0;

  return [{ json: { status: "SUCCESS", contacts_found: count } }];

} catch (err) {
  return [{ json: { status: "FAILED", error: err.message, url: url } }];
}
