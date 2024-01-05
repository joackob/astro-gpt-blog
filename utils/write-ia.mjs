import { exec } from "./exec.mjs";
import fs from "fs";

const seeds = [
	{
		title: "Como conseguir más vistas en LinkedIn",
		description:
			"En este post te mostraremos los mejores tips para rankear primero en las busquedas de recluters",
	},
];

seeds.forEach((seed) => {
	try {
		exec(`cd ia && pipenv run start "${seed.title}" "${seed.description}"`);
		fs.renameSync(
			`./ia/${seed.title.toLowerCase().replace(/ /g, "-")}.md`,
			`./src/content/post/${seed.title.toLowerCase().replace(/ /g, "-")}.mdx`,
		);
		exec(`git add . && git commit -m "add new post: ${seed.title}" && git push`);
	} catch (error) {
		console.log(error);
	}
});
