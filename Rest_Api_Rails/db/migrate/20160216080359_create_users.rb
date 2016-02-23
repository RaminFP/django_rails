class CreateUsers < ActiveRecord::Migration
  def up
    create_table :users do |t|

      t.integer "member_id"
      t.string "firstname", :limit => 30
      t.string "lastname" , :limit => 30
      t.string "password" , :limit => 30
      t.string "confirmpassword" , :limit => 30
      t.string "email" , :limit => 30
      t.boolean "is_active" , :default => false
      t.timestamps null: false
    end

    add_index("users","member_id")
  end

  def down
    drop_table :users
  end
end
