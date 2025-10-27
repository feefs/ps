use eyre::Result;
use std::{env, fs};

const INPUT_FILE_NAME: &str = "input.txt";

pub(super) fn pull_input(session: &str, year: i32, day: u32) -> Result<()> {
    let resp: String = ureq::get(&format!("https://adventofcode.com/{year}/day/{day}/input"))
        .header("Cookie", &format!("session={session}"))
        .call()?
        .body_mut()
        .read_to_string()?;

    fs::write(env::current_dir()?.join(INPUT_FILE_NAME), resp)?;

    Ok(())
}
