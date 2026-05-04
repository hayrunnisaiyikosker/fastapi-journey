## 1. **Connection Management** — How does your connection manager track connected clients? What happens if a client disconnects mid-vote? Does your app handle this gracefully, or does it crash?
Every vote page has a unique poll_id .The connection manager controlling with this way the connection and active WebSocket. If someone wants to join the system adding to them on list, if connection fail they are becaming out of the list. There is no crash because websocket has a try/except conditon.

## 2. **State Storage** — You are storing vote counts in memory. Why did you choose this over writing votes to a database? What breaks if you restart the server? What would need to change to make this production-ready?
We chose in-memory storage instead of a database because database needs installation and this is mini-project that's why we do not need to store data. When restore the server RAM will be clean, all polls and votes will lost. To make production ready, we would need to use a database like PostgreSQL or MongoDB to persist the data.

## 3. **Concurrency** — What would happen if two users voted at exactly the same moment? Did you handle this in your implementation? If not, what is the risk?
when two users voted at the same moment  for example; both server will read 5 and both add 1, both of them will write 6 , and result become as a 6 but correct result must be 7 so 1 vote lost. I did not handle this in my implementation to be honest. To fix this in production, we would need to use asyncio.Lock() to ensure only one vote is processed at a time.

## 4. **REST vs WebSocket** — You now have two ways to vote: `POST /polls/{id}/vote` and the WebSocket. What is the key difference in behavior between them? When would a client prefer one over the other?
When you vote with the Rest `POST /polls/{id}/vote`, you can see the result but other Other open tabs not updated. It was just for one time request-respose cycle. When you vote with WebSocket, this is working with broadcast and which related all windows will update. WebSocket is preferred when multiple users are watching the same poll at the same time and need to see live updates.
