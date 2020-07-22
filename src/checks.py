def category_robotics(ctx):
    return ctx.channel.category.name.lower() == "robotics facility"


def chan(ctx, name):
    return ctx.channel.name == name


def chan_staff(ctx):
    return chan(ctx, "staff")


def chan_commands(ctx):
    return chan(ctx, "bot-commands")


def chan_assignment(ctx):
    return chan(ctx, "role-assignment")


def chan_log(ctx):
    return chan(ctx, "redbot_log")
