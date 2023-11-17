import { execSync } from "child_process";
import fs from "fs";

const seeds = [
	{
		title: "Consejos para mejorar tu salud mental",
		description:
			"Encuentra consejos útiles y prácticos para cuidar tu bienestar mental en el día a día.",
	},
	{
		title: "Recetas saludables y fáciles de preparar",
		description:
			"Explora una variedad de recetas deliciosas que son saludables y simples de cocinar en casa.",
	},
	{
		title: "El impacto de la tecnología en la educación",
		description:
			"Analiza cómo la tecnología ha transformado la educación y su influencia en el aprendizaje moderno.",
	},
	{
		title: "Consejos para mejorar tus habilidades de escritura",
		description:
			"Descubre estrategias efectivas para perfeccionar tu escritura y comunicarte de manera más clara y persuasiva.",
	},
	{
		title: "Innovaciones en el mundo de la inteligencia artificial",
		description:
			"Explora los avances más recientes en inteligencia artificial y su impacto en diferentes aspectos de la vida cotidiana.",
	},
	{
		title: "Ideas creativas para decorar tu hogar",
		description:
			"Inspírate con ideas creativas y prácticas para decorar tu hogar y hacerlo más acogedor.",
	},
	{
		title: "El arte de la fotografía: consejos para principiantes",
		description:
			"Aprende los conceptos básicos de la fotografía y obtén consejos útiles para capturar imágenes impresionantes.",
	},
	{
		title: "Cómo cultivar un jardín en espacios reducidos",
		description:
			"Descubre técnicas y consejos para cultivar un jardín hermoso incluso si cuentas con poco espacio disponible.",
	},
	{
		title: "Los beneficios de adoptar un estilo de vida minimalista",
		description:
			"Explora los beneficios físicos y mentales de vivir con menos y adoptar un enfoque minimalista en la vida cotidiana.",
	},
	{
		title: "Cómo empezar un negocio en línea",
		description:
			"Aprende los pasos fundamentales para lanzar y hacer crecer un negocio exitoso en el entorno digital.",
	},
	{
		title: "Consejos para mejorar la concentración y el enfoque",
		description:
			"Descubre estrategias efectivas para aumentar tu concentración y mejorar tu capacidad de enfoque en tus actividades diarias.",
	},
	{
		title: "Hábitos nocturnos para tener un mejor día",
		description:
			"Explora hábitos nocturnos que pueden mejorar tu productividad y bienestar durante el día siguiente.",
	},
];

const exec = (cmd) => {
	execSync(cmd, { stdio: "inherit" });
};

seeds.forEach((seed) => {
	try {
		exec(`cd ia && pipenv run start "${seed.title}" "${seed.description}"`);
		fs.renameSync(
			`./ia/${seed.title.toLowerCase().replace(/ /g, "-")}.md`,
			`./src/content/post/${seed.title.toLowerCase().replace(/ /g, "-")}.mdx`,
		);
	} catch (error) {
		console.log(error);
	}
});
