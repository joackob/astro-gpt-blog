import { execSync } from "child_process";

const exec = (cmd) => {
	execSync(cmd, { stdio: "inherit" });
};

export { exec };
