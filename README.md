A fork of 9003's flag uploader, that I modified to satisfy a few wants I had

- Uses the same TOML file as Shine/Henson
- Randomly selects flags out of the flags folder

# Usage
If you use Shine, copy in your `config.toml` file.

If you do not use Shine, create a `config.toml` file with the following format
```toml
[nations]
"nation_name" = "password"
"another_nation" = "another password"
```
Additionally, `NSDotPY` and `rtoml` are requirements. So run `pip3 install -r requirements.txt`

Populate the `flags` directory with the flags you would like to apply to your puppets

Run `flag_upload.py`, then press space until you're done.