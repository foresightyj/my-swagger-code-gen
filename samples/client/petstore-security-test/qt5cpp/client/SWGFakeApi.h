/**
 * Swagger Petstore *_/ ' \" =end -- \\r\\n \\n \\r
 * This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  *_/ ' \" =end --       
 *
 * OpenAPI spec version: 1.0.0 *_/ ' \" =end -- \\r\\n \\n \\r
 * Contact: apiteam@swagger.io *_/ ' \" =end -- \\r\\n \\n \\r
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */

#ifndef _SWG_SWGFakeApi_H_
#define _SWG_SWGFakeApi_H_

#include "SWGHttpRequest.h"

#include <QString>

#include <QObject>

namespace Swagger {

class SWGFakeApi: public QObject {
    Q_OBJECT

public:
    SWGFakeApi();
    SWGFakeApi(QString host, QString basePath);
    ~SWGFakeApi();

    QString host;
    QString basePath;

    void testCodeInject */ &#39; &quot; &#x3D;end  \r\n \n \r(QString* test_code_inject____end____rn_n_r);
    
private:
    void testCodeInject */ &#39; &quot; &#x3D;end  \r\n \n \rCallback (HttpRequestWorker * worker);
    
signals:
    void testCodeInject */ &#39; &quot; &#x3D;end  \r\n \n \rSignal();
    
    void testCodeInject */ &#39; &quot; &#x3D;end  \r\n \n \rSignalE(QNetworkReply::NetworkError error_type, QString& error_str);
    
};

}
#endif
