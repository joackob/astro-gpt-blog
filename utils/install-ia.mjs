import { exec } from "./exec.mjs";

exec("echo 'installing ia deps...'");
exec("cd ia && pipenv install");
