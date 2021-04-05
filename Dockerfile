FROM golang:alpine AS builder

RUN apk update && apk upgrade && \
    apk add --no-cache bash git openssh

COPY . .
RUN GO111MODULE=auto go get -d
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 GO111MODULE=auto go build -o /go/bin/main


FROM scratch

COPY --from=builder /go/bin/main /
COPY --from=builder /templates /
COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/ca-certificates.crt

CMD ["/main"]