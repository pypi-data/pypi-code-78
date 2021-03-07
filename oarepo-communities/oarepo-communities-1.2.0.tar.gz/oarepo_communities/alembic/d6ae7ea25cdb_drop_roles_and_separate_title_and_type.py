#
# This file is part of Invenio.
# Copyright (C) 2016-2018 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Drop roles and separate title and type."""
import sqlalchemy as sa
import sqlalchemy_utils
from alembic import op

# revision identifiers, used by Alembic.
from oarepo_communities.models import OAREPO_COMMUNITIES_TYPES

revision = 'd6ae7ea25cdb'
down_revision = '3e42ba8102a0'
branch_labels = ()
depends_on = None


def upgrade():
    """Upgrade database."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('oarepo_communities', sa.Column('title', sa.String(length=128), nullable=True))
    op.add_column('oarepo_communities',
                  sa.Column('type',
                            sqlalchemy_utils.types.choice.ChoiceType(
                                choices=OAREPO_COMMUNITIES_TYPES, impl=sa.CHAR(length=16)),
                            nullable=False))
    op.drop_constraint('fk_oarepo_communities_curators_id_accounts_role', 'oarepo_communities', type_='foreignkey')
    op.drop_constraint('fk_oarepo_communities_publishers_id_accounts_role', 'oarepo_communities', type_='foreignkey')
    op.drop_constraint('fk_oarepo_communities_members_id_accounts_role', 'oarepo_communities', type_='foreignkey')
    op.drop_column('oarepo_communities', 'curators_id')
    op.drop_column('oarepo_communities', 'members_id')
    op.drop_column('oarepo_communities', 'publishers_id')
    # ### end Alembic commands ###


def downgrade():
    """Downgrade database."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('oarepo_communities', sa.Column('publishers_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('oarepo_communities', sa.Column('members_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('oarepo_communities', sa.Column('curators_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('fk_oarepo_communities_members_id_accounts_role', 'oarepo_communities', 'accounts_role',
                          ['members_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key('fk_oarepo_communities_publishers_id_accounts_role', 'oarepo_communities', 'accounts_role',
                          ['publishers_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key('fk_oarepo_communities_curators_id_accounts_role', 'oarepo_communities', 'accounts_role',
                          ['curators_id'], ['id'], ondelete='CASCADE')
    op.drop_column('oarepo_communities', 'type')
    op.drop_column('oarepo_communities', 'title')
    # ### end Alembic commands ###
