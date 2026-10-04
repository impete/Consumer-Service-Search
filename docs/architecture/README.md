# Architecture overview

1. User submits service type, location, radius, and ranking preference.
2. Web/mobile client calls the Node.js API.
3. The API calls the Python search service over HTTP.
4. The search service queries PostgreSQL and ranks results; Redis caches repeat queries.
5. The API returns a ranked list.
