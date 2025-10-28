// Contact form
const contactForm = document.getElementById("contactForm");
const contactSuccess = document.getElementById("contactSuccess");

contactForm.addEventListener("submit", async (e) => {
  e.preventDefault(); // prevent page reload

  const formData = new FormData(contactForm);

  try {
    const response = await fetch("/contact", {
      method: "POST",
      body: formData,
    });

    const data = await response.json();

    if (data.status === "Success") {
      // show thank you popup
      contactSuccess.classList.add("show");

      // clear form
      contactForm.reset();

      // hide popup after 4 seconds
      setTimeout(() => {
        contactSuccess.classList.remove("show");
      }, 4000);
    } else {
      alert("Error: " + data.message);
    }
  } catch (err) {
    console.error(err);
    alert("Something went wrong submitting the form.");
  }
});
