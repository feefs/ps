use clap::{Parser, Subcommand};

#[derive(Parser)]
#[clap(about, version)]
pub(super) struct Cli {
    #[clap(subcommand)]
    pub(super) command: Option<CliCommands>,
    /// Year of the puzzle, current year EST if not specified
    pub(super) year: Option<i32>,
    /// Day of the puzzle, current day EST if not specified
    pub(super) day: Option<u32>,
}

#[derive(Subcommand)]
pub(super) enum CliCommands {
    /// Interact with the authentication config
    Config {
        #[clap(short, long)]
        /// Set session token
        set_session: bool,
    },
}
