const statusEl = document.getElementById("serverStatus");
const messagesEl = document.getElementById("messages");
const feedbackEl = document.getElementById("feedback");

async function checkServer() {
  try {
    const response = await fetch("/api/health");
    const data = await response.json();
    statusEl.textContent = data.status;
    statusEl.classList.add("online");
  } catch (error) {
    statusEl.textContent = "Server unavailable";
    statusEl.classList.remove("online");
  }
}

async function loadMessages() {
  messagesEl.innerHTML = "<p>Loading messages…</p>";
  try {
    const response = await fetch("/api/messages");
    const data = await response.json();
    if (!data.success) throw new Error("Could not retrieve messages.");
    messagesEl.innerHTML = "";
    if (data.messages.length === 0) {
      messagesEl.innerHTML = "<p>No messages yet. Send the first one.</p>";
      return;
    }
    data.messages.slice().reverse().forEach(item => {
      const card = document.createElement("article");
      card.className = "message";
      const name = document.createElement("strong");
      name.textContent = item.name;
      const message = document.createElement("p");
      message.textContent = item.message;
      card.append(name, message);
      messagesEl.appendChild(card);
    });
  } catch (error) {
    messagesEl.textContent = "Could not connect to the server. Check that server.py is running.";
  }
}

document.getElementById("messageForm").addEventListener("submit", async event => {
  event.preventDefault();
  feedbackEl.textContent = "Sending…";
  feedbackEl.classList.remove("error");
  const payload = {
    name: document.getElementById("name").value,
    message: document.getElementById("message").value
  };
  try {
    const response = await fetch("/api/messages", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });
    const data = await response.json();
    if (!response.ok || !data.success) throw new Error(data.error || "Message was not sent.");
    feedbackEl.textContent = "Success! The server received your message.";
    document.getElementById("message").value = "";
    await loadMessages();
  } catch (error) {
    feedbackEl.textContent = error.message;
    feedbackEl.classList.add("error");
  }
});

document.getElementById("refreshButton").addEventListener("click", loadMessages);
checkServer();
loadMessages();
