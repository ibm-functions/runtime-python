/*
 * Copyright 2023 IBM Corporation
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package integration

import common._
import common.rest.WskRestOperations
import org.junit.runner.RunWith
import org.scalatest.junit.JUnitRunner
import java.io.File
import spray.json._
import scala.io.Source
import org.scalatest.BeforeAndAfterAll

@RunWith(classOf[JUnitRunner])
class CredentialsIBMPythonCOSTests extends TestHelpers with WskTestHelpers with BeforeAndAfterAll with WskActorSystem {

  lazy val defaultKind = Some("python:3.6")

  implicit val wskprops: WskProps = WskProps()
  val wsk = new WskRestOperations
  val datdir = "tests/dat/cos"
  val actionName = "testCOSService"
  val actionFileName = "testCOSService.py"

  // read credentials from from vcap_services.json
  val vcapFile = WhiskProperties.getProperty("vcap.services.file")
  val vcapString = Source.fromFile(vcapFile).getLines.mkString
  val vcapInfo =
    JsonParser(ParserInput(vcapString)).asJsObject.fields("cloud-object-storage").asInstanceOf[JsArray].elements(0)
  val creds = vcapInfo.asJsObject.fields("credentials").asJsObject

  val apikey = creds.fields("apikey").asInstanceOf[JsString]

  var resource_instance_id = creds.fields("resource_instance_id").asInstanceOf[JsString]

  val __bx_creds = JsObject(
    "cloud-object-storage" -> JsObject("apikey" -> apikey, "resource_instance_id" -> resource_instance_id))

  it should "Test connection to Cloud Object Storage COS on IBM Cloud" in withAssetCleaner(wskprops) {
    (wp, assetHelper) =>
      val file = Some(new File(datdir, actionFileName).toString())

      assetHelper.withCleaner(wsk.action, actionName) { (action, _) =>
        action.create(
          actionName,
          file,
          main = Some("main"),
          kind = defaultKind,
          parameters = Map("__bx_creds" -> __bx_creds))
      }
      withActivation(wsk.activation, wsk.action.invoke(actionName)) { activation =>
        val response = activation.response
        response.result.get.fields.get("error") shouldBe empty
        response.result.get.fields.get("data") should be(
          Some(JsString("This is a test file for IBM-Functions integration testing.")))
      }
  }
}
