"""Changes in models

Revision ID: 27aa9f4bfbde
Revises: d4867f3a4c0a
Create Date: 2021-01-18 19:26:32.645619

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '27aa9f4bfbde'
down_revision = 'd4867f3a4c0a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('line',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_line_description'), 'line', ['description'], unique=False)
    op.create_index(op.f('ix_line_id'), 'line', ['id'], unique=False)
    op.create_index(op.f('ix_line_title'), 'line', ['title'], unique=False)
    op.create_table('lineitem',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('line_id', sa.Integer(), nullable=False),
    sa.Column('item_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['item_id'], ['item.id'], ),
    sa.ForeignKeyConstraint(['line_id'], ['line.id'], ),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id', 'line_id', 'item_id')
    )
    op.add_column('item', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('item', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.add_column('user', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('user', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('user', 'hashed_password',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'hashed_password',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_column('user', 'updated_at')
    op.drop_column('user', 'created_at')
    op.drop_column('item', 'updated_at')
    op.drop_column('item', 'created_at')
    op.drop_table('lineitem')
    op.drop_index(op.f('ix_line_title'), table_name='line')
    op.drop_index(op.f('ix_line_id'), table_name='line')
    op.drop_index(op.f('ix_line_description'), table_name='line')
    op.drop_table('line')
    # ### end Alembic commands ###
