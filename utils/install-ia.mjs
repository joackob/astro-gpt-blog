import { execSync } from "child_process";

const exec = (cmd) => {
	execSync(cmd, { stdio: "inherit" });
};

exec("echo 'installing ia deps...'");
exec("cd ia && pip install -r requirements.txt");
