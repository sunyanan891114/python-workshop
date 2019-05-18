const jsonServer = require('json-server')
const server = jsonServer.create()
const middlewares = jsonServer.defaults()
const attachmentRoute = jsonServer.router('./static/accachment.json');
const iterationRoute = jsonServer.router('./static/iteration.json');
const bugRoute = jsonServer.router('./static/bug.json');

server.use(middlewares)

server.use(jsonServer.rewriter({
    '/tracker/busibness/getIterationTrackerWorkitem\\?iterationUuid=:iterationUuid\\&pblId=': '/iteration/:iterationUuid',
    '/tracker/attachment/queryAttachFile\\?referenceId=:referenceId\\&type=:type': '/attachment/:referenceId',
    '/tracker/busibness/getWiDefect\\?filedAgainst=:filedAgainst\\&*': '/bug/:filedAgainst'
}))

server.use('/iteration', iterationRoute)
server.use('/attachment', attachmentRoute)
server.use('/bug', bugRoute)

server.listen(3000, () => {
    console.log('JSON Server is running')
})