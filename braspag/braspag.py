import base64
import json
import requests


def converter_base_64(client_id, client_secret):
    '''
    Recebe: client_id, client_secret
    Retorna: as duas strings concatenadas e convertidas em Base64
    '''
    conc = client_id + ":" + client_secret  # Concatena strings
    enc = base64.b64encode(conc.encode())  # Codifica para bytes e Base64
    authorization = "Basic " + enc.decode()  # Decodifica de bytes para string
    return authorization


def obter_token(authorization):
    '''
    Obtém um token que é usado para autenticar na API Slit da Cielo
    Esse token tem validade de 20 minutos e deverá ser obtido um novo sempre que expirar.
    Recebe: client_id, client_secret concatenados e convertidos em Base64
    Retorna: Token para acesso a API Split
    '''
    url = "https://authsandbox.braspag.com.br/oauth2/token"
    headers = {
        "Authorization": authorization,
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {"grant_type": "client_credentials"}
    token = requests.post(
        url,
        data=data,
        headers=headers
    )

    return token.json()["access_token"]


class Braspag:
    tk = ''

    def __init__(self, access_token, sandbox=True):
        self.sandbox = sandbox

        self.return_url = 'http://www.braspag.com.br'
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + access_token,

        }

        if self.sandbox is True:
            self.transacionalUrl = "https://apisandbox.cieloecommerce.cielo.com.br"
        else:
            self.transacionalUrl = "https://api.cieloecommerce.cielo.com.br"

    def autorizacao(self, orderId, nomeCliente, cpf, valor, numeroCartao,
                    nomePortador, dataVencimento, codSeguranca, bandeira,
                    motoristaBraspagId, salvar=False):
        '''
        Cria primeira autorização.
        Devolve json com os dados da autorização
        Se salvar for True, retorna token que pode ser
        usado para salvar o cartão.
        '''
        values = {
            "merchantorderid": orderId,
            "customer": {
                "Name": nomeCliente,
                "Identity": cpf,
                "identitytype": "CPF",
            },
            "payment": {
                "type": "splittedcreditcard",
                "amount": valor,
                "capture": False,
                "installments": 1,
                "CreditCard": {
                    "cardNumber": numeroCartao,
                    "holder": nomePortador,
                    "ExpirationDate": dataVencimento,
                    "SecurityCode": codSeguranca,
                    "Brand": bandeira,
                    "SaveCard": salvar
                },
                "fraudanalysis": {
                    "provider": "cybersource",
                    "Shipping": {
                        "Addressee": nomeCliente
                    },
                    "totalorderamount": valor,
                },
                "splitpayments": [
                    {
                        "subordinatemerchantid": motoristaBraspagId,
                        "amount": valor,
                    },
                ]
            }
        }

        service_url = f"{self.transacionalUrl}/1/sales/"
        print(self.headers)
        pagamento = requests.post(
            service_url,
            data=json.dumps(values),

            headers=self.headers
        )

        return pagamento.json()

    def autorizacaoComToken(self, orderId, nomeCliente, cpf,
                            valor, token, codSeguranca, bandeira,
                            motoristaBraspagId):
        '''
        Cria primeiro pagamento com Alias já cadastrado.
        Devolve json com os dados do pagamento.
        '''
        values = {
            "merchantorderid": orderId,
            "customer": {
                "Name": nomeCliente,
                "Identity": cpf,
                "identitytype": "CPF",
            },
            "payment": {
                "type": "splittedcreditcard",
                "amount": valor,
                "installments": 1,
                "capture": False,
                "CreditCard": {
                    "CardToken": token,
                    "SecurityCode": codSeguranca,
                    "Brand": bandeira,
                },
                "fraudanalysis": {
                    "provider": "cybersource",
                    "Shipping": {
                        "Addressee": nomeCliente
                    },
                    "totalorderamount": valor,
                },
                "splitpayments": [
                    {
                        "subordinatemerchantid": motoristaBraspagId,
                        "amount": valor,
                    },
                ]
            },
        }

        service_url = f"{self.transacionalUrl}/1/sales/"

        pagamento = requests.post(
            service_url,
            data=json.dumps(values),
            headers=self.headers
        )
        print(pagamento.json())
        return pagamento.json()

    def autorizacaoDebito(self, orderId, nomeCliente, cpf, valor, numeroCartao,
                          nomePortador, dataVencimento, codSeguranca, bandeira,
                          motoristaBraspagId, salvar=False):
        values = {
            "merchantorderid": orderId,
            "customer": {
                "Name": nomeCliente,
                "Identity": cpf,
                "identitytype": "CPF",
            },
            "payment": {
                "type": "splitteddebitcard",
                "amount": valor,
                "capture": False,
                "installments": 1,
                "ReturnUrl": self.return_url,
                "debitcard": {
                    "cardnumber": numeroCartao,
                    "holder": nomePortador,
                    "expirationdate": dataVencimento,
                    "securitycode": codSeguranca,
                    "brand": bandeira,
                    "savecard": salvar
                },
                "SplitPayments": [
                    {
                        "subordinatemerchantid": motoristaBraspagId,
                        "amount": valor,
                    },
                ]
            }
        }

        service_url = f"{self.transacionalUrl}/1/sales/"

        pagamento = requests.post(
            service_url,
            data=json.dumps(values),
            headers=self.headers
        )
        return pagamento.json()

    def autorizacaoDebitoComToken(self, orderId, nomeCliente, cpf,
                                  valor, token, codSeguranca, bandeira,
                                  motoristaBraspagId):
        values = {
            "merchantorderid": orderId,
            "customer": {
                "Name": nomeCliente,
                "Identity": cpf,
                "identitytype": "CPF",
            },
            "payment": {
                "type": "splitteddebitcard",
                "amount": valor,
                "capture": False,
                "installments": 1,
                "ReturnUrl": self.return_url,
                "debitcard": {
                    "CardToken": token,
                    "SecurityCode": codSeguranca,
                    "Brand": bandeira,
                },
                "SplitPayments": [
                    {
                        "subordinatemerchantid": motoristaBraspagId,
                        "amount": valor,
                    },
                ]
            }
        }

        service_url = f"{self.transacionalUrl}/1/sales/"

        pagamento = requests.post(
            service_url,
            data=json.dumps(values),
            headers=self.headers
        )
        return pagamento.json()

    def captura(self, paymentId, valor, motoristaBraspagId):
        '''
        Recebe o id do pagamento e faz a captura
        '''
        data = {
            "SplitPayments": [
                {
                    "SubordinateMerchantId": motoristaBraspagId,
                    "Amount": valor,
                    "Fares": {
                        "Mdr": 0,
                        "Fee": 0
                    }
                },
            ]
        }
        service_url = \
            f'{self.transacionalUrl}/1/sales/{paymentId}/capture'
        captura = requests.put(
            service_url,
            data=json.dumps(data),
            headers=self.headers,
        )
        return captura.json()


class Onboarding:
    def __init__(self, access_token, sandbox=True):
        self.access_token = access_token
        self.sandbox = sandbox
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.access_token,
        }
        if self.sandbox is True:
            self.transacionalUrl = "https://splitonboardingsandbox.braspag.com.br"
        else:
            self.transacionalUrl = "https://splitonboarding.braspag.com.br"

    def cadastro(self, razao_social, nome_fantasia, numero_documento,
                 tipo_documento, mcc, nome_contato, telefone, email,
                 codigo_banco, tipo_conta, numero_conta, dig_verif,
                 agencia, digito_agencia, documento_conta, tipo_doc_conta,
                 rua, numero, complemento, bairro, cidade, estado, cep):
        '''
        Cadastra novo subordinado na api de pagamentos.
        Os dados a serem passados podem ser consultados em:
        https://braspag.github.io/manual/split-pagamentos-braspag-onboarding#informando-a-porcentagem-do-mdr-%C3%BAnico-aplicado-para-todos-os-acordos

        '''
        data = {
            "CorporateName": razao_social,
            "FancyName": nome_fantasia,
            "DocumentNumber": numero_documento,
            "DocumentType": tipo_documento,
            "MerchantCategoryCode": mcc,
            "ContactName": nome_contato,
            "ContactPhone": telefone,
            "MailAddress": email,
            "BankAccount": {
                "Bank": codigo_banco,
                "BankAccountType": tipo_conta,
                "Number": numero_conta,
                "VerifierDigit": dig_verif,
                "AgencyNumber": agencia,
                "AgencyDigit": digito_agencia,
                "DocumentNumber": documento_conta,
                "DocumentType": tipo_doc_conta,
            },
            "Address": {
                "Street": rua,
                "Number": numero,
                "Complement": complemento,
                "Neighborhood": bairro,
                "City": cidade,
                "State": estado,
                "ZipCode": cep,
            },
            "Agreement": {
                "Fee": 0,
                "MdrPercentage": 0
            },
            "Notification": {
                "Url": "https://site.com.br/api/subordinados",
                "Headers": [{
                    "Key": "key1",
                    "Value": "value1"
                },
                    {
                        "Key": "key2",
                        "Value": "value2"
                    }]
            },
        }

        service_url = f"{self.transacionalUrl}/api/subordinates"
        cadastro = requests.post(
            service_url,
            data=json.dumps(data),
            headers=self.headers
        )
        return cadastro.json()

    def consulta(self, subordinate_merchant_id):
        service_url = \
            f'{self.transacionalUrl}/api/subordinates/{subordinate_merchant_id}'
        resultado = requests.get(
            service_url,
            headers=self.headers,
        )
        try:
            return resultado.json()
        except Exception as e:
            print(e)
            return resultado
