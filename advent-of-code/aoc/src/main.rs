mod cli;
mod config;
mod pull;

use cli::{Cli, CliCommands};

use ansi_term::Color;
use chrono::{Datelike, Utc};
use chrono_tz::US::Eastern;
use clap::Parser;
use eyre::Result;
use std::process::ExitCode;

fn aoc() -> Result<()> {
    let c = Cli::parse();

    if let Some(CliCommands::Config { set_session }) = c.command {
        if set_session {
            config::write_auth()?;
            println!("{}", Color::Green.paint("New session token set!"));
        } else {
            println!("{}", config::auth_path()?.display());
        }
        return Ok(());
    }

    let eastern_datetime = Utc::now().with_timezone(&Eastern);
    let year = c.year.unwrap_or(eastern_datetime.year());
    let day = c.day.unwrap_or(eastern_datetime.day());

    let auth = config::get_auth()?;
    pull::pull_input(&auth.session, year, day)?;
    println!(
        "{}",
        Color::Green.paint(format!(
            "Successfully pulled input for year {year} day {day}!",
        )),
    );

    Ok(())
}

fn main() -> ExitCode {
    match aoc() {
        Ok(()) => ExitCode::SUCCESS,
        Err(error) => {
            println!("{} {error}", Color::Red.paint("Error:"));
            ExitCode::FAILURE
        }
    }
}
