from discord import utils, Member, Role
import logging
import os


def init_logging(debug):
	logger = logging.getLogger(__name__)
	logger.addHandler(logging.StreamHandler())
	logger.setLevel(logging.DEBUG if debug else logging.INFO)
	return logger


def env(key, default=None):
	return os.environ.get(key, default)


async def get_role_by_name(ctx, name):
	if role := utils.find(lambda m: m.name == name, ctx.guild.roles):
		return role
	else:
		raise AttributeError(f"Role '{name}' could not be found.")


async def toggle_role(member: Member, role: Role):
	if role in member.roles:
		await member.remove_roles(role)
		return False
	await member.add_roles(role)
	return True
