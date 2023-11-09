import { execSync } from "child_process";

const exec = (cmd) => {
	execSync(cmd, { stdio: "inherit" });
};

exec("cd ia && pipenv run start");
exec("mv ./ia/*.md ./src/content/post/");
