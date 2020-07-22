from discord import utils, Member, Role
import logging
import os
import datetime


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


def time_to_weekly_event(day=0, hour=0, minute=0, second=0):
	current_time = datetime.datetime.now(tz=datetime.timezone.utc)
	current_day = datetime.timedelta(days=current_time.weekday())

	# Reference time; Monday, 00:00 UTC
	reference_time = current_time.replace(hour=0, minute=0, second=0, microsecond=0) - current_day

	# Delta between reference time and target
	target_offset = datetime.timedelta(days=day, hours=hour, minutes=minute, seconds=second)

	# Datetime of event, not corrected for passed events
	target_time = reference_time + target_offset

	# 1 week delta, to correct for passed events
	week_offset = datetime.timedelta(days=7)

	# Datetime of next event
	next_event = target_time + week_offset*(target_time < current_time)

	# Delta between current time and next event
	next_offset = next_event - current_time
	return next_offset.total_seconds()
