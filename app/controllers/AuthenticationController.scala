package controllers

import javax.inject.{Inject, Singleton}
import play.api.mvc.{AbstractController, ControllerComponents}
 
import play.api.libs.json._
// you need this import to have combinators
import play.api.libs.functional.syntax._

class AuthenticationController @Inject()(cc: ControllerComponents) extends AbstractController(cc) {


  implicit val rds = (
    (__ \ 'name).read[String] and
      (__ \ 'age).read[Long]
    ) tupled
  def signUp = Action {

    Ok(views.html.index("Here's your sign up page"))
  }

  def login =  Action { request =>
    request.body.asJson.map { json =>
      json.validate[(String, Long)].map{
        case (name, age) => Ok("Hello " + name + ", you're "+age)
      }.recoverTotal{
        e => BadRequest("Detected error:"+ JsError.toFlatJson(e))
      }
    }.getOrElse {
      BadRequest("Expecting Json data")
    }
  }

}
