"""empty message

Revision ID: 21262fb370b1
Revises: 45b023fe18e7
Create Date: 2024-11-15 11:39:54.609759

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '21262fb370b1'
down_revision = '45b023fe18e7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('delivery_riders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('telegram_token', sa.String(length=100), nullable=True),
    sa.Column('phone_number', sa.String(length=15), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('successful_deliveries', sa.Integer(), nullable=True),
    sa.Column('last_seen', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('phone_number')
    )
    op.create_table('order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user', sa.String(), nullable=True),
    sa.Column('phone', sa.String(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('order', sa.String(), nullable=True),
    sa.Column('notes', sa.String(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('date_confirmed', sa.DateTime(), nullable=True),
    sa.Column('date_delivered', sa.DateTime(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('paid', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order')
    op.drop_table('delivery_riders')
    # ### end Alembic commands ###