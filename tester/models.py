from django.db import models




class CommentReaction(models.Model):
    def __init__(self, comment_id, reaction):
        self.comment_id = comment_id
        self.reaction = reaction
