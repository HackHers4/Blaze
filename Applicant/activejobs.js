// Simulate getting status from backend
  let status = "selected"; // Change this to "Selected" or "Declined" to test

  const button = document.getElementById("statusButton");

  // Update button based on status
  switch(status.toLowerCase()) {
    case "selected":
      button.textContent = "Selected";
      button.classList.add("status-selected");
      break;
    case "declined":
      button.textContent = "Declined";
      button.classList.add("status-declined");
      break;
    case "in review":
    default:
      button.textContent = "In Review";
      button.classList.add("status-review");
      break;
  }