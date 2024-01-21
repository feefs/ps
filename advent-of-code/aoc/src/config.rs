use eyre::Result;
use inquire::{Password, PasswordDisplayMode};
use serde::{Deserialize, Serialize};
use std::{fs, path::PathBuf};
use xdg::BaseDirectories;

const PKG_NAME: &str = env!("CARGO_PKG_NAME");

#[derive(Deserialize, Serialize)]
pub(super) struct Auth {
    pub(super) session: String,
}

pub(super) fn auth_path() -> Result<PathBuf> {
    Ok(BaseDirectories::with_prefix(PKG_NAME)?.place_config_file("auth.toml")?)
}

pub(super) fn write_auth() -> Result<()> {
    let session = Password::new("Input session token:")
        .with_display_mode(PasswordDisplayMode::Masked)
        .prompt()?;

    let contents = toml::to_string_pretty(&Auth { session })?;
    fs::write(auth_path()?, contents)?;

    Ok(())
}

pub(super) fn get_auth() -> Result<Auth> {
    let path = auth_path()?;

    if !path.try_exists()? {
        write_auth()?;
    }

    let contents = fs::read_to_string(path)?;
    Ok(toml::from_str::<Auth>(&contents)?)
}
