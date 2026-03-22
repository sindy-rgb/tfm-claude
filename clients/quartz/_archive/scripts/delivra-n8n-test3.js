// TEST — this node MUST receive input from another node for $http to work
// Connect a Manual Trigger → this node

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

  var count = Array.isArray(resp) ? resp.length : 0;
  return [{ json: { status: "SUCCESS", contacts_found: count } }];

} catch (err) {
  return [{ json: { status: "FAILED", error: err.message } }];
}
