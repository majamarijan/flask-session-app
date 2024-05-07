window.onload = () => {
	const form = document.querySelector("form") || null;
	const themeBtn = document.querySelector("input[type='checkbox']");

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
	if (window.localStorage.getItem("theme")) {
		let theme = window.localStorage.getItem("theme");
		document.body.classList.add(theme);
		themeBtn.checked = true;
	}
	themeController(themeBtn);
};

function themeController(themeBtn) {
	themeBtn.addEventListener("change", (e) => {
		if (themeBtn.checked) {
			document.body.classList.add("dark");
			window.localStorage.setItem("theme", "dark");
		} else {
			document.body.classList.remove("dark");
			window.localStorage.removeItem("theme");
		}
	});
}
