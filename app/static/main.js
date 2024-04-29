window.onload = () => {
	const form = document.querySelector("form") || null;
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
};
