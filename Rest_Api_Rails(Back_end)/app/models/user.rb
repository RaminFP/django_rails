class User < ActiveRecord::Base

  belongs_to :member

  scope :search ,lambda {|query|
                  where(["firstname LIKE ?","%#{query}%"])
                }


end
