# Random-User-Generator

This repository contains a simple Python script to generate a list of random users using the Faker library. The script can be used as a standalone script or imported as a module in other projects.

## Requirements
- Python 3.x
- Faker library : Install it using `pip install Faker`

## Usage
### Standalone script
To generate a list of random users, run the `user.py` script:

By default, the script will generate and print a list of 5 random users. You can modify the number of users to generate by changing the `n` parameter in the `get_users` function call.

### Import as a module
You can also import the `get_users` function from the user module in your own Python scripts. To do so, add the following line to your script:

`from user import get_users`

Then, you can call the `get_users` function with the desired number of users to generate:

```
users = get_users(10)
print(users)
```

### Logging
The `user` module logs the user generation process to a `user.log` file located in the same directory as the script. This log file includes information about the number of users generated and the time of the generation.

## Contributing
Contributions to improve the script or fix bugs are welcome. Please feel free to submit a pull request or open an issue to discuss any changes or report problems.

## License
This project is released under the MIT License.
