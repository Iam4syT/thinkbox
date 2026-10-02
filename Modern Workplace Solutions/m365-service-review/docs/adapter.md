# Read-only adapter orientation — unimplemented and unrun

Official documentation checked 30 September 2026; exact lab steps and URLs are in LAB.md. No Graph client, app registration, tenant consent or credentials exist in this package.

Health orientation: GET v1.0 `/admin/serviceAnnouncement/healthOverviews?$expand=issues`, with the documented ServiceHealth.Read.All permission and approved work/school identity. Follow every returned nextLink. Provider service labels must be mapped to the reviewed subscribed workloads, with coverage declared; do not assume OneDrive always appears as a separately named provider service. Unknown/new statuses remain incomplete until explicitly mapped and tested.

Usage orientation: GET `/reports/getSharePointSiteUsageDetail(period='D7')` with Reports.Read.All and the appropriate reporting role. The API returns a short-lived report download redirect; it is not the health JSON schema. Keep its URL/export private. Record refresh date, byte units, window and identifier masking. Current usage of a new test tenant may be delayed or absent. Separate Teams activity/denominator observations require their own authorised source and consistent reporting window.

Audit orientation: use the approved Purview Audit search and licence/role/collection boundary. The local demo's severity labels do not implement audit classification. A missing collection cannot be encoded as an empty complete audit result.

Required before claiming a live adapter: exact schema mapping, complete pagination, freshness, privacy, role denial, throttling/retry and manual reconciliation of normal/review conditions. Retain raw exports privately and publish only checked synthetic derivatives. This guidance is a plan, not integration evidence.
