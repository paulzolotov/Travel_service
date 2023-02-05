
from django.db.models import signals
from django.dispatch import receiver
from .models import Game, Category


@receiver(signals.post_save, sender=Game)
def create_game(sender, instance, created, **kwargs):
	if created:
		category = instance.category
		category.games_amount += 1
		category.save()


@receiver(signals.post_delete, sender=Game)
def delete_game(sender, instance, using, **kwargs):
	category = instance.category
	category.games_amount -= 1
	category.save()
