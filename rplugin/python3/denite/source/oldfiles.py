# -*- coding: utf-8 -*-
# FILE: oldfiles.py

from os import path
from .base import Base

class Source(Base):

    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'oldfiles'
        self.kind = 'file'

    def gather_candidates(self, context):
        return [
            {'word': x, 'action__path': x}
            for x in self.vim.eval('v:oldfiles') if path.isfile(x)
        ]
