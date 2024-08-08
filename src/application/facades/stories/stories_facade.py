from application.bases.base_facade import BaseUseCaseFacade

from application.usecases.stories.stories import CreateStory, ListStoriesForUser, RetrieveStory, ListStoriesForAuthor


class StoriesFacade(BaseUseCaseFacade):
    async def create(self, author_id, title, text, tags_ids):
        return await CreateStory(self.uow)(author_id, title, text, tags_ids)

    async def stories_for_user(self, user_id, tags_ids):
        return await ListStoriesForUser(self.uow)(user_id, tags_ids)

    async def story_retrieve(self, story_id):
        return await RetrieveStory(self.uow)(story_id)

    async def stories_for_author(self, user_id):
        return await ListStoriesForAuthor(self.uow)(user_id)
