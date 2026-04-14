description = [[
Gets basic HTTP server info like status, server header and page title
]]

author = "student"
categories = {"default", "safe"}

portrule = function(host, port)
    return port.protocol == "tcp" and (port.number == 80 or port.number == 8080)
end

action = function(host, port)

    local http = require "http"
    local response = http.get(host, port, "/")

    if not response then
        return "no response"
    end

    local server = response.header["server"] or "not found"
    local status = response.status or "unknown"

    local title = "not found"
    if response.body then
        title = response.body:match("<title>(.-)</title>") or "not found"
    end

    return "Status: " .. status ..
           "\nServer: " .. server ..
           "\nTitle: " .. title
end