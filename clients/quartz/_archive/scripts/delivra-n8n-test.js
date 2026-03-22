// MINIMAL TEST — just one API call, return whatever happens
var url = "https://integration.delivra.com/DelivraRESTServices/Services.svc/Categories/623803/Contacts";

try {
  var resp = await $http.request({
    method: "GET",
    url: url,
    headers: {
      "username": "aroggio+newsletter-ops@qz.com",
      "password": "N3ws-Qu@rtz-Ops",
      "listname": "quartz-prod"
    },
    json: true
  });

  var count = 0;
  if (Array.isArray(resp)) {
    count = resp.length;
  }

  return [{ json: { status: "SUCCESS", contacts_found: count, first_contact: resp[0] || "none" } }];

} catch (err) {
  return [{ json: { status: "FAILED", error: err.message, url: url } }];
}
