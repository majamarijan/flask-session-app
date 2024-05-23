let html, themeBtn;


document.addEventListener("DOMContentLoaded", ready);

function ready() {
	// when images, css and scripts are not yet loaded, only DOM tree is built
	// document.querySelector('main').innerHTML = 'Loading...'
	document.querySelector('#themeBtn').innerHTML = window.localStorage.getItem("theme") === "light" ? "Dark" : "Light";
	document.querySelector('html').setAttribute("data-theme", window.localStorage.getItem("theme") ? window.localStorage.getItem("theme") : "light");
}
window.onload = () => {
	console.log("loaded");
	const form = document.querySelector("form") || null;
	const themeBtn = document.querySelector("#themeBtn") || null;
	const html = document.querySelector("html");

	if (form) {
		let data = {};
		form.onsubmit = (e) => {
			e.preventDefault();
			const fdata = new FormData(form);
			for (var [key, value] of fdata) {
				data[key] = value;
			}
			const res = fetch(window.location.origin + "/submit", {
				method: "POST",
				redirect: "follow",
				headers: {
					"Content-Type": "application/json",
				},
				body: JSON.stringify(data),
			}).then((d) => {
				window.location.href = d.url;
			});
		};
	}

	if (themeBtn) themeBtn.onclick = (e) => switchTheme(e, html);


	if (window.localStorage.getItem("theme") === "light") {
		themeBtn.innerHTML = "Dark";
		html.setAttribute("data-theme", "light");
	} else {
		themeBtn.innerHTML = "Light";
		html.setAttribute("data-theme", "dark");
	}

};

async function switchTheme(e, html) {
	if (e.target.innerHTML === "Light") {
		e.target.innerHTML = "Dark";
		window.localStorage.setItem("theme", "light");
		html.setAttribute("data-theme", "light");
	} else {
		e.target.innerHTML = "Light";
		window.localStorage.setItem("theme", "dark");
		html.setAttribute("data-theme", "dark");
	}
}


