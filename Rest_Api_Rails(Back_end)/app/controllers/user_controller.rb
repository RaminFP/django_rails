class UserController < ApplicationController

  require 'json'
  require 'base64'

  def index

    begin
      @selectuser = User.all
      render json: @selectuser
    rescue => ex
      logger.error ex.message
    end
  end

  def search

    begin
      @getname = params[:name]
      @search2db = User.search(@getname)
      render json: @search2db
    rescue => ex
      logger.error ex.message
    end
  end

  def create

    begin

      @getModel = params[:model]
      @decode_model = Base64.decode64(@getModel)
      @Convert2hash = JSON[@decode_model]
      usr = User.new(:member_id => @Convert2hash['mem_id'],:firstname => @Convert2hash['firstname'],:lastname => @Convert2hash['lastname'],:password => @Convert2hash['password'],:confirmpassword => @Convert2hash['confpassword'],:email => @Convert2hash['email'] ,:is_active => @Convert2hash['is_active'])
      if usr
        usr.save
      end

    rescue => ex
      logger.error ex.message

    end

  end

  def edit

    begin

      @getIDEdit = params[:editID]
      @getModelEdit = params[:modeledit]
      @DecodeEdit = Base64.decode64(@getModelEdit)
      @Convert2hash = JSON[@DecodeEdit]
      @finduser2edit = User.find(@getIDEdit)
      @finduser2edit.update(:member_id => @Convert2hash['mem_id'],:firstname => @Convert2hash['firstname'],:lastname => @Convert2hash['lastname'],:password => @Convert2hash['password'],:confirmpassword => @Convert2hash['confpassword'],:email => @Convert2hash['email'] ,:is_active => @Convert2hash['is_active'])
      @finduser2edit.save

    rescue => ex
      logger.error ex.message
    end
  end

  def delete

    begin

      @getID = params[:id]
      @finaldelete = User.find(@getID)
      @finaldelete.destroy

    rescue => ex
      logger.error ex.message
    end
  end

end
