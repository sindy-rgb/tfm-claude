var CONFIG = {
  BASE_URL: "https://integration.delivra.com/DelivraRESTServices/Services.svc",
  USERNAME: "aroggio+newsletter-ops@qz.com",
  PASSWORD: "N3ws-Qu@rtz-Ops",
  LISTNAME: "quartz-prod",
  AGENCIES: [
    { name: "TFM", category_id: 623803, category_name: "feed-media" },
    { name: "BG", category_id: 623802, category_name: "boletin" },
    { name: "GL", category_id: 601833, category_name: "paid-acquisition" }
  ],
  BAKEOFF_START: "2026-02-01",
  CONTACT_SAMPLE_SIZE: 100
};

return [{ json: CONFIG }];
