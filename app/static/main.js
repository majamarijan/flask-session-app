window.onload = () => {
	const form = document.querySelector("form") || null;
	const themeBtn = document.querySelector("input[type='checkbox']");
	let theme = '';

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
		let currentTheme = window.localStorage.getItem("theme");
		document.body.classList.add(currentTheme);
		themeBtn.checked = currentTheme === 'dark' ? true : false;
		theme = currentTheme;
	}
	window.localStorage.setItem('theme',theme)
	themeController(themeBtn, theme);
};

function themeController(themeBtn, theme) {
	themeBtn.addEventListener("change", (e) => {
		console.log()
		if(themeBtn.checked) {
			document.body.classList.add('dark');
			window.localStorage.setItem('theme', 'dark');
		}else {
			document.body.classList.remove('dark');
			window.localStorage.setItem('theme','light')
		}
	});
}
