function toggleDescription(element) {
    const paragraph = element.previousElementSibling;
    if (element.textContent === "View More") {
        paragraph.style.display = "block";
        element.textContent = "View Less";
    } else {
        paragraph.style.display = "-webkit-box";
        element.textContent = "View More";
    }
}

// Initialize paragraphs to show only a snippet
document.querySelectorAll(".dm-serif-display-regular").forEach(p => {
    p.style.display = "-webkit-box";
    p.style.webkitBoxOrient = "vertical";
    p.style.webkitLineClamp = "3";
    p.style.overflow = "hidden";
});
