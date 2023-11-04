"""empty message

Revision ID: 47c536442220
Revises: 
Create Date: 2023-10-26 09:37:37.134553

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '47c536442220'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('delivery_agent',
    sa.Column('first_name', sa.String(length=20), nullable=False),
    sa.Column('last_name', sa.String(length=30), nullable=False),
    sa.Column('date_of_birth', sa.Date(), nullable=False),
    sa.Column('gender', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('is_email_verified', sa.Boolean(), nullable=False),
    sa.Column('password', sa.String(length=60), nullable=False),
    sa.Column('phone_number', sa.String(length=15), nullable=False),
    sa.Column('contact_address', sa.String(length=200), nullable=False),
    sa.Column('drivers_license_number', sa.String(length=10), nullable=False),
    sa.Column('license_expiration_date', sa.Date(), nullable=False),
    sa.Column('license_image_file', sa.LargeBinary(), nullable=False),
    sa.Column('id', sa.String(length=60), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('drivers_license_number'),
    sa.UniqueConstraint('email')
    )
    op.create_table('user',
    sa.Column('first_name', sa.String(length=20), nullable=False),
    sa.Column('last_name', sa.String(length=30), nullable=False),
    sa.Column('gender', sa.String(length=20), nullable=False),
    sa.Column('date_of_birth', sa.Date(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('is_email_verified', sa.Boolean(), nullable=False),
    sa.Column('password', sa.String(length=60), nullable=False),
    sa.Column('phone_number', sa.String(length=15), nullable=False),
    sa.Column('contact_address', sa.String(length=200), nullable=False),
    sa.Column('user_type', sa.String(length=30), nullable=True),
    sa.Column('id', sa.String(length=60), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('delivery_request',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('agent_id', sa.Integer(), nullable=True),
    sa.Column('pickup_address', sa.String(length=200), nullable=False),
    sa.Column('pickup_time', sa.DateTime(), nullable=False),
    sa.Column('item_description', sa.String(length=50), nullable=False),
    sa.Column('contact_person', sa.String(length=50), nullable=False),
    sa.Column('contact_phone_number', sa.String(length=15), nullable=False),
    sa.Column('delivery_address', sa.String(length=200), nullable=False),
    sa.Column('delivery_time', sa.DateTime(), nullable=False),
    sa.Column('delivery_instruction', sa.String(length=400), nullable=True),
    sa.Column('estimated_distance', sa.String(length=15), nullable=False),
    sa.Column('estimated_duration', sa.String(length=15), nullable=False),
    sa.Column('delivery_cost', sa.String(length=20), nullable=False),
    sa.Column('order_status', sa.String(length=20), nullable=False),
    sa.Column('id', sa.String(length=60), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['agent_id'], ['delivery_agent.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('delivery_request')
    op.drop_table('user')
    op.drop_table('delivery_agent')
    # ### end Alembic commands ###