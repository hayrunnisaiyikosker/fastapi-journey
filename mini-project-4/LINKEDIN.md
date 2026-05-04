## LinkedIn Post Text
Built a Real-Time Polling App with FastAPI & WebSockets

For my latest mini project, I developed a real-time polling system where votes are reflected instantly across multiple browser tabs — without any page refresh.

The application includes a full REST API for creating, listing, retrieving, and deleting polls. However, the core feature of this project is the WebSocket-based real-time communication. Whenever a user votes, the update is broadcast instantly to all connected clients, ensuring a seamless live experience.

One issue I encountered was that my test interface wasn’t updating in real time. After debugging, I realized I was opening the HTML file directly via file://, which prevented the WebSocket connection from working properly. Serving the page through a FastAPI endpoint (/test) resolved the problem and enabled real-time updates across multiple tabs.

Additionally, I containerized the entire application using Docker, making it easy to run the project in any environment with a single command.

Through this project, I gained hands-on experience with:

The difference between REST (request-response) and WebSockets (persistent communication)

Managing multiple active connections using a connection manager

Broadcasting real-time updates to connected clients

You can check out the project here: [GitHub Branch Link]

#FastAPI #WebSockets #BackendDevelopment #Python #100DaysOfCode



https://github.com/hayrunnisaiyikosker/fastapi-journey/tree/hiyikosker-mini-project-4

## LinkedIn Post URL
https://www.linkedin.com/posts/hayrunnisa-iyik%C3%B6%C5%9Fker-922b95309_fastapi-websockets-backenddevelopment-ugcPost-7457188819625246720-HIJo?utm_source=share&utm_medium=member_desktop&rcm=ACoAAE6p0-oBH1MaajrWgEHrQ1c7Z4Qg2_qLd4U