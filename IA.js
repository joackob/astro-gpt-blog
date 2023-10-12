const API_KEY = "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";

// eslint-disable-next-line @typescript-eslint/no-unused-vars
async function getCompletion(prompt) {
	const response = await fetch(`https://api.openai.com/v1/completions`, {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
			Authorization: `Bearer ${API_KEY}`,
		},
		body: JSON.stringify({
			model: "text-davinci-003",
			/* prompt: "give a random example of programming language"*/
			prompt: "Dame 10 ejemplos de peliculas",
			max_tokens: 20,
		}),
	});
	console.log("soy la ia");
	const data = await response.json();
	console.log(data);
}
getCompletion("Dame 10 ejemplos de peliculas");
