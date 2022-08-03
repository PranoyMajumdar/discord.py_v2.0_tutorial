# **Hybrid command example**

#### @commands.hybrid_command(name='Ping', with_app_command=True, description='Shows the bot latency.')

<br>

## Parameters:
- name (str) – The name to create the command with. By default this uses the function name unchanged.

- with_app_command (bool) – Whether to register the command as an application command.

- **attrs – Keyword arguments to pass into the construction of the hybrid command


<br>


#### @commands.hybrid_group(name='channel', with_app_command=True, description='Parent command of channel')

## Parameters:
- name (str) – The name to create the command with. By default this uses the function name unchanged.

- with_app_command (bool) – Whether to register the command as an application command.

- **attrs – Keyword arguments to pass into the construction of the hybrid command

##### @channel.command(name='create', description='Create a channel')

- name (str) – The name to create the command with. By default this uses the function name unchanged.
