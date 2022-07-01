class MessageSerialiser {
    set_source(source: string): this {
        // ...
        return this;
    }

    set_timestamp(timestamp: Date): this {
        // ...
        return this;
    }

    as_bytes(): Uint8Array {
        // ...
    }
}


class RequestSerialiser extends MessageSerialiser {
    set_request_param(param: string): this {
        // ...
        return this;
    }
}


const message = (
    new RequestSerialiser()
    .set_source('My PC')
    .set_timestamp(new Date())
    .set_request_param('give me the data!')
    .as_bytes())
